'''
    Copyright (C) 2019 Gitcoin Core

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
from django.conf import settings
from django.utils import translation

from marketing.mails import setup_lang, send_mail
from marketing.utils import should_suppress_notification_email, func_name
from ptokens.emails import render_personal_token_created, render_personal_token_redeem_accepted, \
    render_personal_token_redeem_rejected, render_personal_token_redeem_requested, \
    render_personal_token_redeem_complete_sender, render_personal_token_redeem_complete_receiver


def personal_token_created(profile, ptoken):
    from_email = settings.CONTACT_EMAIL
    to_email = profile.email
    if not to_email:
        if profile and profile.user:
            to_email = profile.user.email
    if not to_email:
        return

    cur_language = translation.get_language()

    try:
        setup_lang(to_email)
        html, text, subject = render_personal_token_created(ptoken)

        if not should_suppress_notification_email(to_email, 'personal_token_created'):
            send_mail(from_email, to_email, subject, text, html, categories=['transactional', func_name()])
    finally:
        translation.activate(cur_language)


def personal_token_redeem_requested(profile, ptoken, redeem):
    from_email = settings.CONTACT_EMAIL
    to_email = profile.email
    if not to_email:
        if profile and profile.user:
            to_email = profile.user.email
    if not to_email:
        return

    cur_language = translation.get_language()

    try:
        setup_lang(to_email)
        html, text, subject = render_personal_token_redeem_requested(ptoken, redeem)

        if not should_suppress_notification_email(to_email, 'personal_token_created'):
            send_mail(from_email, to_email, subject, text, html, categories=['transactional', func_name()])
    finally:
        translation.activate(cur_language)


def personal_token_redeem_accepted(profile, ptoken, redeem):
    from_email = settings.CONTACT_EMAIL
    to_email = profile.email
    if not to_email:
        if profile and profile.user:
            to_email = profile.user.email
    if not to_email:
        return

    cur_language = translation.get_language()

    try:
        setup_lang(to_email)
        html, text, subject = render_personal_token_redeem_accepted(ptoken, redeem)

        if not should_suppress_notification_email(to_email, 'personal_token_created'):
            send_mail(from_email, to_email, subject, text, html, categories=['transactional', func_name()])
    finally:
        translation.activate(cur_language)


def personal_token_redeem_rejected(profile, ptoken, redeem):
    from_email = settings.CONTACT_EMAIL
    to_email = profile.email
    if not to_email:
        if profile and profile.user:
            to_email = profile.user.email
    if not to_email:
        return

    cur_language = translation.get_language()

    try:
        setup_lang(to_email)
        html, text, subject = render_personal_token_redeem_rejected(ptoken, redeem)

        if not should_suppress_notification_email(to_email, 'personal_token_created'):
            send_mail(from_email, to_email, subject, text, html, categories=['transactional', func_name()])
    finally:
        translation.activate(cur_language)


def personal_token_redeem_complete_sender(profile, ptoken, redeem):
    from_email = settings.CONTACT_EMAIL
    to_email = profile.email
    if not to_email:
        if profile and profile.user:
            to_email = profile.user.email
    if not to_email:
        return

    cur_language = translation.get_language()

    try:
        setup_lang(to_email)
        html, text, subject = render_personal_token_redeem_complete_sender(ptoken, redeem)

        if not should_suppress_notification_email(to_email, 'personal_token_created'):
            send_mail(from_email, to_email, subject, text, html, categories=['transactional', func_name()])
    finally:
        translation.activate(cur_language)


def personal_token_redeem_complete_receiver(profile, ptoken, redeem):
    from_email = settings.CONTACT_EMAIL
    to_email = profile.email
    if not to_email:
        if profile and profile.user:
            to_email = profile.user.email
    if not to_email:
        return

    cur_language = translation.get_language()

    try:
        setup_lang(to_email)
        html, text, subject = render_personal_token_redeem_complete_receiver(ptoken, redeem)

        if not should_suppress_notification_email(to_email, 'personal_token_created'):
            send_mail(from_email, to_email, subject, text, html, categories=['transactional', func_name()])
    finally:
        translation.activate(cur_language)
