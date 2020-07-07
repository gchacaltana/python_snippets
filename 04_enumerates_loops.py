# !/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # Lista de cuentas de Twitter
    twitter_accounts = ('@AndrewYNg','@ylecun','@solodatascience','@solocodigoweb','@DataScienceCtrl','@gchacaltanab')

    # Iteramos la lista "twitter_accounts"
    for key,value in enumerate(twitter_accounts):
        print(f'Key: {key} - Account Name: {value}')

    # Devuelve:
    # Key: 0 - Account Name: @AndrewYNg
    # Key: 1 - Account Name: @ylecun
    # Key: 2 - Account Name: @solodatascience
    # Key: 3 - Account Name: @solocodigoweb
    # Key: 4 - Account Name: @DataScienceCtrl
    # Key: 5 - Account Name: @gchacaltanab

    print(f"\n")
    # Inicializamos el contador en 298090
    for key,value in enumerate(twitter_accounts,298090):
        print(f'Account ID: {key} - Account Name: {value}')

    # Devuelve:
    # Account ID: 298090 - Account Name: @AndrewYNg
    # Account ID: 298091 - Account Name: @ylecun
    # Account ID: 298092 - Account Name: @solodatascience
    # Account ID: 298093 - Account Name: @solocodigoweb
    # Account ID: 298094 - Account Name: @DataScienceCtrl
    # Account ID: 298095 - Account Name: @gchacaltanab
