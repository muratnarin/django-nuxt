from django.core.management.base import BaseCommand

from project.models import Parameter, ParameterGroup, Country, City,Blog
from django.template.defaultfilters import slugify

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_parameter_groups()
        self.create_currency_parameters()
        self.create_country_and_city()
        self.create_school_types()
        self.create_blog_posts()

    def create_parameter_groups(self):
        self.stdout.write(self.style.NOTICE('Default parameter Groups migrating...'))
        default_parameter_groups = [
            {'name': 'currency_type', 'display_name_tr': 'Para Birimi', 'display_name_en': 'Currency'},
            {'name': 'country', 'display_name_tr': 'Ülke', 'display_name_en': 'Country'},
            {'name': 'city', 'display_name_tr': 'Şehir', 'display_name_en': 'City'},
            {'name': 'type', 'display_name_tr': 'Okul Türü', 'display_name_en': 'School Type'},

        ]

        for pg in default_parameter_groups:
            ParameterGroup.objects.get_or_create(**pg, operation_user=1)

    def create_school_types(self):
        self.stdout.write(self.style.NOTICE('School Types parameters migrating...'))
        parameter_group = ParameterGroup.objects.get(name="type")
        types = [
            {'code': 1, 'name': 'uni', 'display_name_tr': 'Üniversite', 'display_name_en': 'Univesity'},
            {'code': 2, 'name': 'lise', 'display_name_tr': 'Lise', 'display_name_en': 'High School'},
            {'code': 3, 'name': 'sertifika', 'display_name_tr': 'Sertifika', 'display_name_en': 'Certificate'},
            {'code': 4, 'name': 'dil_okulu', 'display_name_tr': 'Dil Okulu', 'display_name_en': 'Language School'},
            {'code': 5, 'name': 'staj', 'display_name_tr': 'Staj', 'display_name_en': 'Internship'}
        ]

        if parameter_group:
            for i in types:
                Parameter.objects.get_or_create(parameter_group=parameter_group,
                                                name=i['name'],
                                                code=i['code'],
                                                display_name_tr=i['display_name_tr'],
                                                display_name_en=i['display_name_en'],
                                                is_active=True)

    def create_country_and_city(self):
        self.stdout.write(self.style.NOTICE('Country and city migrating...'))
        import json
        f = open("data/countries_cities.json")
        data = json.load(f)
        # print(data)
        for i in data:
            country = Country.objects.get_or_create(
                name_tr=i["translations"]["tr"],
                name_en=i["name"],
                iso2=i["iso2"],
                iso3=i["iso3"],
                numeric_code=i["numeric_code"],
                phone_code=i["phone_code"],
                capital=i["capital"],
                currency=i["currency"],
                currency_name=i["currency_name"],
                currency_symbol=i["currency_symbol"],
                native=i["native"],
                region=i["region"],
                subregion=i["subregion"],
                latitude=i["latitude"],
                longitude=i["longitude"],
                emoji=i["emoji"],
            )
            for city in i['cities']:
                City.objects.get_or_create(
                    name=city['name'],
                    country=country[0],
                    latitude=city['latitude'],
                    longitude=city['longitude']
                )

        f.close()

    def create_currency_parameters(self):
        self.stdout.write(self.style.NOTICE('Currency parameters migrating...'))
        parameter_group = ParameterGroup.objects.get(name="currency_type")
        currency = [
            {'code': 1, 'name': 'TL', 'display_name_tr': 'TL'},
            {'code': 2, 'name': 'USD', 'display_name_tr': 'USD'},
            {'code': 3, 'name': 'EUR', 'display_name_tr': 'EUR'},
            {'code': 4, 'name': 'GBP', 'display_name_tr': 'GBP'},
            {'code': 5, 'name': 'CHF', 'display_name_tr': 'CHF'},
            {'code': 6, 'name': 'AZN', 'display_name_tr': 'AZN'},
            {'code': 7, 'name': 'MKD', 'display_name_tr': 'MKD'},
            {'code': 8, 'name': 'TMT', 'display_name_tr': 'TMT'},
            {'code': 9, 'name': 'GEL', 'display_name_tr': 'GEL'},
            {'code': 10, 'name': 'RUB', 'display_name_tr': 'RUB'},
            {'code': 11, 'name': 'BGN', 'display_name_tr': 'BGN'},
            {'code': 12, 'name': 'CAD', 'display_name_tr': 'CAD'},
            {'code': 13, 'name': 'AUD', 'display_name_tr': 'AUD'},
            {'code': 14, 'name': 'IRR', 'display_name_tr': 'IRR'},
            {'code': 15, 'name': 'IQD', 'display_name_tr': 'IQD'},
            {'code': 16, 'name': 'SAR', 'display_name_tr': 'SAR'},
            {'code': 17, 'name': 'AED', 'display_name_tr': 'AED'},
            {'code': 18, 'name': 'MRO', 'display_name_tr': 'MRO'},
            {'code': 19, 'name': 'CNY', 'display_name_tr': 'CNY'},
            {'code': 20, 'name': 'LEI', 'display_name_tr': 'LEI'},
            {'code': 21, 'name': 'SUM', 'display_name_tr': 'SUM'},
            {'code': 22, 'name': 'PLN', 'display_name_tr': 'PLN'},
            {'code': 23, 'name': 'KZT', 'display_name_tr': 'KZT'},
            {'code': 24, 'name': 'DKK', 'display_name_tr': 'DKK'},
            {'code': 25, 'name': 'JPY', 'display_name_tr': 'JPY'},
            {'code': 26, 'name': 'MAD', 'display_name_tr': 'MAD'},
            {'code': 27, 'name': 'TZS', 'display_name_tr': 'TZS'},
            {'code': 28, 'name': 'NOK', 'display_name_tr': 'NOK'},
            {'code': 29, 'name': 'SEK', 'display_name_tr': 'SEK'},
            {'code': 30, 'name': 'KWD', 'display_name_tr': 'KWD'},
            {'code': 31, 'name': 'MXN', 'display_name_tr': 'MXN'},
            {'code': 32, 'name': 'HUF', 'display_name_tr': 'HUF'},
            {'code': 33, 'name': 'KGS', 'display_name_tr': 'KGS'},
            {'code': 34, 'name': 'BRL', 'display_name_tr': 'BRL'},
            {'code': 35, 'name': 'DZD', 'display_name_tr': 'DZD'},
            {'code': 36, 'name': 'QAR', 'display_name_tr': 'QAR'},
            {'code': 37, 'name': 'NGN', 'display_name_tr': 'NGN'},
            {'code': 38, 'name': 'GHS', 'display_name_tr': 'GHS'},
            {'code': 39, 'name': 'PEN', 'display_name_tr': 'PEN'},
            {'code': 40, 'name': 'XAU', 'display_name_tr': 'XAU'},
            {'code': 41, 'name': 'AOA', 'display_name_tr': 'AOA'},
            {'code': 42, 'name': 'BAM', 'display_name_tr': 'BAM'},
            {'code': 43, 'name': 'CFA', 'display_name_tr': 'CFA'},
            {'code': 44, 'name': 'MDL', 'display_name_tr': 'MDL'},
        ]

        if parameter_group:
            for i in currency:
                Parameter.objects.get_or_create(parameter_group=parameter_group, name=i['name'],
                                                display_name_tr=i['display_name_tr'],
                                                display_name_en=i['display_name_tr'],
                                                is_active=True)

    def create_blog_posts(self):
        self.stdout.write(self.style.NOTICE('Blog Posts migrating...'))
        import xlrd
        from datetime import datetime
        loc = ("data/blogPosts.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        for row in range(sheet.nrows):
            if row==0:
                continue
            title_tr = sheet.cell_value(row, 0)
            title_en = sheet.cell_value(row, 1)
            description_tr = sheet.cell_value(row, 2)
            description_en = sheet.cell_value(row, 3)
            date = sheet.cell_value(row, 4)
            date = date.replace(" ", "") \
                .replace("Nisan", ".04.") \
                .replace("Mayıs", ".05.") \
                .replace("Ocak", ".01.") \
                .replace("Şubat", ".02.") \
                .replace("Mart", ".03.") \
                .replace("Haziran", ".06.") \
                .replace("Temmuz", ".07.") \
                .replace("Ağustos", ".08.") \
                .replace("Eylül", ".09.") \
                .replace("Ekim", ".10.") \
                .replace("Kasım", ".11.") \
                .replace("Aralık", ".12.")
            date = datetime.strptime(date, '%d.%m.%Y')
            Blog.objects.get_or_create(
                title_tr=title_tr,
                title_en=title_en,
                description_tr=description_tr,
                description_en=description_en,
                date=date.date(),
                slug=slugify(title_en) if title_en else slugify(title_tr)
            )


