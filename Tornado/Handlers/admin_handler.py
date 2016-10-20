#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dateutil.parser

import requests
import tornado.web
from models import *
import jdatetime
import json


class add_buy_Handler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        info = json.loads(self.request.body)
        payer_id = info['payer_id']
        amount = info['amount']
        concern = info['concern']
        partners = info['partners']
        id_admin = int(info['id_admin'])
        date = dateutil.parser.parse(info['date'])
        bool_accept = info['bool_accept']
        per_share = int(info['per_share'])

        if not bool_accept:
            buy = Buy.create(
                amount=amount,
                concern=concern,
                date=date,
                payer_id=payer_id,
                per_share=per_share
            )
            for i in partners:
                User_has_buy.create(
                    User=i,
                    Buy=buy.id
                )

            for i in partners:
                try:
                    find_user = User.select().where(User.User == id_admin, User.id == i).get()
                    find_user = find_user.account
                except:
                    find_user = False
                account2 = per_share + int(find_user)
                update_account = User.update(account=account2).where(User.User == id_admin, User.id == i)
                update_account.execute()

        self.respond(data='success')

    def respond(self, data, code=200):
        self.set_status(code)
        self.write(json.dumps({
            "status": code,
            "data": data
        }))
        self.finish()
