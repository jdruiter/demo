# coding: utf-8

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import translation
from django.core.mail.message import EmailMultiAlternatives
from wkhtmltopdf.views import PDFTemplateResponse

import logging
logger = logging.getLogger('emails')


class EmailTemplate(models.Model):
    pass


def replace_invoice_vars(message, invoice, language='nl'):
    '''Replace variables in an invoice (email) text'''

    if language and translation.check_for_language(language):
        translation.activate(language)

    message = message \
        .replace('%invoice%', str(invoice)) \
        .replace('%invoice_nr%', str(invoice.invoice_nr)) \
        .replace('%type%', str(invoice.type) or '') \
        .replace('%status%', str(invoice.status) or '') \
        .replace('%SKU%', str(invoice.SKU) or '') \
        .replace('%name%', str(invoice.name) or '') \
        .replace('%quantity%', str(invoice.quantity) or '') \
        .replace('%price%', str(invoice.price) or '') \
        .replace('%start_date%', str(invoice.start_date_print) or '') \
        .replace('%commission_perc%', str(invoice.commission_perc) or '') \
        .replace('%fixed_commission%', str(invoice.fixed_commission) or '') \
        .replace('%tax_area%', str(invoice.tax_area_display) or '') \
        .replace('%total%', str(invoice.total) or '') \
        .replace('%commission_amount%', str(invoice.commission_amount) or '') \
        .replace('%commission_VAT%', str(invoice.commission_VAT) or '') \
        .replace('%commission_total%', str(invoice.commission_total) or '') \
        .replace('%payable_amount%', str(invoice.payable_amount) or '') \
        .replace('%invoice_link%', str(invoice.invoice_link) or '') \
        .replace('%invoice_link_pdf%', str(invoice.invoice_link_pdf) or '')

    return message


def send_invoice(invoice):
    """
    Sends Invoice to the invoice partner
    """

    template = EmailTemplate.objects.get(name='invoice-email')
    subject         = replace_invoice_vars(template.subject, invoice, 'en')
    message_plain   = replace_invoice_vars(template.plain_text, invoice, 'en')
    message_html    = replace_invoice_vars(template.html_text, invoice, 'en')

    partner_email = invoice.partner.partner_email or invoice.partner.finance_email

    msg = EmailMultiAlternatives(
        subject=subject,
        body=message_plain,
        from_email='info@adventuretickets.nl',
        to=[partner_email, ],
        bcc=['finance@adventuretickets.nl'],
    )
    msg.attach_alternative(message_html, 'text/html')

    # make Invoice PDF
    cmd_options = {
        'orientation': 'landscape',
        'page-size': 'A4',
        'title': invoice.invoice_nr
    }

    template = 'adventures/invoice/invoice_pdf.html'
    context = {
        'invoice': invoice,
        'partner': invoice.partner,
    }

    pdf_data = PDFTemplateResponse(request=None, template=template, context=context, filename=invoice.invoice_nr, show_content_in_browser=True, cmd_options=cmd_options)
    pdf_data.render()
    pdf_data.close()

    filename = "{} invoice Adventure Tickets {}.pdf".format(invoice.created.strftime("%Y-%m-%d"), invoice.invoice_nr)
    msg.attach(filename, pdf_data.rendered_content, 'application/pdf')
    msg.send()
    logger.info("Invoice sent to {}: {}".format(partner_email, str(invoice)))
