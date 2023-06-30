from django.db import models

# Create your models here.
STATE_CHOICES = (
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Nagaland','Nagaland'),
    ('Mizoram','Mizoram'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Telangana','Telangana'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Rajasthan','Rajasthan'),
    ('Punjab','Punjab'),
    ('Goa','Goa'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Bihar','Bihar'),
    ('Puducherry','Puducherry'),
    ('Lakshadweep','Lakshadweep'),
    ('Ladakh ','Ladakh '),
    ('New Delhi ','New Delhi '),
    ('Daman and Diu','Daman and Diu'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Raipur','Raipur')
)
class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False , auto_created=False)
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveBigIntegerField()
    states = models.CharField(choices= STATE_CHOICES, max_length=100)
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg' , blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)


