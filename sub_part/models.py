from django.db import models

# Create your models here.


class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class stdsignin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pwd = models.CharField(max_length=100)
    re_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class clgsignin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pwd = models.CharField(max_length=100)
    re_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class unisignin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pwd = models.CharField(max_length=100)
    re_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class addstd(models.Model):
    sno = models.CharField(max_length=100)
    stdname = models.CharField(max_length=100)
    stdid = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    reg = models.CharField(max_length=100)
    cls = models.CharField(max_length=100)
    sec = models.CharField(max_length=100)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.reg


class course(models.Model):
    cid = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    cd = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class College(models.Model):
    uid = models.CharField(max_length=100)
    cc = models.CharField(max_length=100)
    clgname = models.CharField(max_length=100)
    clgd = models.CharField(max_length=100)

    def __str__(self):
        return self.cc


class stdregister(models.Model):

    fname = models.CharField(max_length=100)

    lname = models.CharField(max_length=100)
    dob = models.DateField(default=None)
    gender = models.CharField(max_length=100)

    fathername = models.CharField(max_length=100)
    pschool = models.CharField(max_length=200, default=None)
    add = models.CharField(max_length=100)

    def __str__(self):
        return self.fname
