# Generated by Django 4.0.5 on 2022-08-31 07:50

from django.db import migrations, models
import fundraisers.models.campaign
import fundraisers.models.fundraisers_medical
import fundraisers.models.fundraisers_others
import fundraisers.models.ngo_registration


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('relation', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('raising_for', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=250)),
                ('aim', models.IntegerField()),
                ('end_date', models.DateField()),
                ('main_pic', models.ImageField(upload_to=fundraisers.models.campaign.Campaign.nameFile)),
                ('cover_photo', models.ImageField(upload_to=fundraisers.models.campaign.Campaign.nameFile)),
                ('story', models.CharField(max_length=750)),
                ('category_tag', models.CharField(max_length=50)),
                ('current_amount_raised', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fundraiser_others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact_number', models.PositiveIntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('street_address', models.CharField(max_length=60)),
                ('street_address1', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('postal_code', models.IntegerField()),
                ('to_whom_fund_raised', models.CharField(max_length=20)),
                ('beneficiary_name', models.CharField(max_length=20)),
                ('beneficiary_contact_number', models.IntegerField()),
                ('beneficiary_age', models.IntegerField()),
                ('beneficiary_sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], max_length=10)),
                ('beneficiary_address', models.CharField(max_length=50)),
                ('beneficiary_address1', models.CharField(blank=True, max_length=50)),
                ('beneficiary_city', models.CharField(max_length=15)),
                ('beneficiary_state', models.CharField(max_length=15)),
                ('beneficiary_postalcode', models.IntegerField()),
                ('title_of_campaign', models.TextField(max_length=100, unique=True)),
                ('beneficiary_story', models.TextField(max_length=300)),
                ('tax_Status', models.CharField(max_length=20, null=True)),
                ('update_check', models.BooleanField(default=False)),
                ('terms_check', models.BooleanField(default=False)),
                ('video', models.FileField(blank=True, upload_to=fundraisers.models.fundraisers_others.Fundraiser_others.nameFile)),
                ('beneficiary_photo', models.ImageField(upload_to=fundraisers.models.fundraisers_others.Fundraiser_others.nameFile)),
                ('document', models.FileField(upload_to=fundraisers.models.fundraisers_others.Fundraiser_others.nameFile)),
                ('target_amount', models.IntegerField()),
                ('end_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fundraisers_medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_file', models.ImageField(upload_to=fundraisers.models.fundraisers_medical.Fundraisers_medical.nameFile)),
                ('cover_photo', models.ImageField(upload_to=fundraisers.models.fundraisers_medical.Fundraisers_medical.nameFile)),
                ('estimation_letter', models.FileField(upload_to=fundraisers.models.fundraisers_medical.Fundraisers_medical.nameFile)),
                ('medical_bill', models.FileField(upload_to=fundraisers.models.fundraisers_medical.Fundraisers_medical.nameFile)),
                ('medical_reports', models.FileField(upload_to=fundraisers.models.fundraisers_medical.Fundraisers_medical.nameFile)),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_age', models.IntegerField()),
                ('patient_address', models.CharField(max_length=250)),
                ('beneficiary', models.CharField(max_length=50)),
                ('relation', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('target_amount', models.IntegerField()),
                ('end_date', models.DateField()),
                ('hospital_name', models.CharField(max_length=50)),
                ('hospital_address', models.CharField(max_length=250)),
                ('medical_ailment', models.CharField(max_length=50)),
                ('current_situation_details', models.CharField(max_length=500)),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_number', models.IntegerField()),
                ('hospital_number', models.IntegerField()),
                ('fundraiser_title', models.CharField(max_length=50)),
                ('fundraiser_description', models.CharField(max_length=600)),
                ('current_amount_raised', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ngo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regulation_certificate', models.ImageField(null=True, upload_to='uploads/ngo_proofs/regulation_certificate')),
                ('certificate_12A', models.ImageField(null=True, upload_to='uploads/ngo_proofs/certificate_12A')),
                ('valid_status', models.BooleanField(default=False)),
                ('type_of_ngo_certificate', models.TextField(max_length=50)),
                ('license_number', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('videos', models.FileField(blank=True, null=True, upload_to='uploads/ngo_proofs/ngo_videos')),
                ('description', models.TextField(max_length=200)),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='uploads/ngo_proofs/ngo_photos')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='uploads/ngo_proofs/ngo_photos')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='uploads/ngo_proofs/ngo_photos')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='uploads/ngo_proofs/ngo_photos')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='uploads/ngo_proofs/ngo_photos')),
                ('address', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('media_links', models.URLField(blank=True)),
                ('created', models.CharField(max_length=100)),
                ('updated', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ngo_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_type', models.CharField(choices=[('trust registered', 'trust registered'), ('society registered', 'society registered'), ('section 8 comapany registered', 'section 8 coampany registered')], default='trust registered', max_length=30)),
                ('organisation_name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(null=True)),
                ('problem_addressing', models.CharField(max_length=160, null=True)),
                ('valid_status', models.CharField(choices=[('approved', 'approved'), ('declined', 'declined'), ('pending', 'pending')], default='pending', max_length=8)),
                ('organisation_address', models.CharField(max_length=200)),
                ('photo', models.FileField(null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('wesite_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('registration_certificate', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('memorandum', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('trust_deed', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('section_8_license', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('article_of_association', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('memorandum_of_association', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('document1_name', models.CharField(blank=True, max_length=20, null=True)),
                ('document1', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('document2_name', models.CharField(blank=True, max_length=20, null=True)),
                ('document2', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('document3_name', models.CharField(blank=True, max_length=20, null=True)),
                ('document3', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
                ('document4_name', models.CharField(blank=True, max_length=20, null=True)),
                ('document4', models.FileField(blank=True, null=True, upload_to=fundraisers.models.ngo_registration.ngo_registration.nameFile)),
            ],
        ),
    ]
