class Utility:
    def __init__(self):
        self.currencies = {
            'USD' : {'name' : 'US Dollar', 'flag' : ':flag_us:'},
            'JPY' : {'name' : 'Japanese Yen', 'flag' : ':flag_jp:'},
            'BGN' : {'name' : 'Bulgarian Lev', 'flag' : ':flag_hu:'},
            'CZK' : {'name' : 'Czech Koruna', 'flag' : ':flag_cz:'},
            'DKK' : {'name' : 'Danish Krone', 'flag' : ':flag_dk:'},
            'GBP' : {'name' : 'Pound Sterling', 'flag' : ':flag_gb:'},
            'HUF' : {'name' : 'Hungarian Forint', 'flag' : ':flag_hu:'},
            'PLN' : {'name' : 'Polish Zloty', 'flag' : ':flag_pl:'},
            'RON' : {'name' : 'Romanian Leu', 'flag' : ':flag_ro:'},
            'SEK' : {'name' : 'Sweedish Krona', 'flag' : ':flag_se:'},
            'CHF' : {'name' : 'Swiss Franc', 'flag' : ':flag_ch:'},
            'ISK' : {'name' : 'Icelandic Krona', 'flag' : ':flag_is:'},
            'NOK' : {'name' : 'Norwegian Krone', 'flag' : ':flag_no:'},
            'HRK' : {'name' : 'Croatian Kuna', 'flag' : ':flag_hr:'},
            'RUB' : {'name' : 'Russian Rouble', 'flag' : ':flag_ru:'},
            'TRY' : {'name' : 'Turkish Lira', 'flag' : ':flag_tr:'},
            'AUD' : {'name' : 'Australian Dollar', 'flag' : ':flag_au:'},
            'BRL' : {'name' : 'Brazilian Real', 'flag' : ':flag_br:'},
            'CAD' : {'name' : 'Canadian Dollar', 'flag' : ':flag_ca:'},
            'CNY' : {'name' : 'Chinese Yuan Renminbi', 'flag' : ':flag_cn:'},
            'HKD' : {'name' : 'Hong Kong Dollar', 'flag' : ':flag_hk:'},
            'IDR' : {'name' : 'Indonesian Rupiah', 'flag' : ':flag_id:'},
            'ILS' : {'name' : 'Israeli Shekel', 'flag' : ':flag_il:'},
            'INR' : {'name' : 'Indian Rupee', 'flag' : ':flag_in:'},
            'KRW' : {'name' : 'South Korean Won', 'flag' : ':flag_kr:'},
            'MXN' : {'name' : 'Mexican Peso','flag' : ':flag_mx:'},
            'MYR' : {'name' : 'Malaysian Ringgit','flag' : ':flag_my:'},
            'NZD' : {'name' : 'New Zealand Dollar','flag' : ':flag_nz:'},
            'PHP' : {'name' : 'Philippine Peso','flag' : ':flag_ph:'},
            'SGD' : {'name' : 'Singapore Dollar','flag' : ':flag_sg:'},
            'THB' : {'name' : 'Thai Baht','flag' : ':flag_th:'},
            'ZAR' : {'name' : 'South African Rand','flag' : ':flag_za:'},
            'EUR' : {'name' : 'Euro', 'flag' : ':flag_eu:'}}


    def exist(self, abbreviation):
        if abbreviation in self.currencies:
            return True
        return False

    def getFullName(self, abbreviation):
        if self.exist(abbreviation):
            return self.currencies[abbreviation]['name']
        return None

    def getFlagEmoji(self, abbreviation):
        if self.exist(abbreviation):
            return self.currencies[abbreviation]['flag']
        return None

