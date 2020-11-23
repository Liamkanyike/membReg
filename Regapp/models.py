from django.db import models
from PIL import Image


# Create your models here.
class Church(models.Model):
	surname = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=100,null=True)
	email = models.EmailField(max_length=100,null=True,blank=True)
	residential_address = models.CharField(max_length=255,null=True, blank=True)
	former_religion = models.CharField(max_length=255,null=True, blank=True)
	postal_address = models.CharField(max_length=25,null=True, blank=True)
	lc1_village = models.CharField(max_length=25,null=True, blank=True)
	lc2_muluka = models.CharField(max_length=25,null=True, blank=True)
	lc3_subcounty = models.CharField(max_length=25,null=True, blank=True)
	county_ssaza = models.CharField(max_length=25,null=True, blank=True)
	district = models.CharField(max_length=25,null=True, blank=True)
	born_again = models.CharField(max_length=25,null=True, blank=True)
	spirit_filled = models.CharField(max_length=25,null=True, blank=True)
	baptised = models.CharField(max_length=25,null=True, blank=True)
	photo = models.FileField(default='default.jpg', upload_to='profile_pics', null=True,blank=True)
	pdf = models.FileField(upload_to='media', null=True,blank=True)

	marital_status = models.CharField(max_length=25,null=True, blank=True)
	highest_level_of_education = models.CharField(max_length=25,null=True, blank=True)
	occupation = models.CharField(max_length=25,null=True, blank=True)
	place_of_work = models.CharField(max_length=25,null=True, blank=True)
	department = models.CharField(max_length=25,null=True, blank=True)
	head_name = models.CharField(max_length=25,null=True, blank=True)
	head_number = models.CharField(max_length=25,null=True, blank=True)

	any_children = models.CharField(max_length=255,null=True, blank=True)
	number_of_children = models.CharField(max_length=255,null=True, blank=True)
	next_of_kin = models.CharField(max_length=255,null=True, blank=True)
	father_name = models.CharField(max_length=255,null=True, blank=True)
	mother_name = models.CharField(max_length=255,null=True, blank=True)

	father_alive = models.CharField(max_length=25,null=True, blank=True)
	mother_alive = models.CharField(max_length=25,null=True, blank=True)


	dob = models.CharField(max_length=25,null=True, blank=True)
	age = models.CharField(max_length=25,null=True, blank=True)
	zone = models.CharField(max_length=25,null=True, blank=True)
	home_lc1 = models.CharField(max_length=25,null=True, blank=True)
	home_village = models.CharField(max_length=25,null=True, blank=True)
	home_district = models.CharField(max_length=25,null=True, blank=True)
	home_subcounty = models.CharField(max_length=25,null=True, blank=True)
	
	

	other_notes = models.CharField(max_length=255,null=True, blank=True)
	registration_date = models.CharField(max_length=255,null=True)
	

	
class Meta:
	db_table = "church"




