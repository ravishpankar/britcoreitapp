from django.db import models
from django.utils import timezone
from metarisk import error
from metarisk import globals

"""RiskType model class"""
class RiskType(models.Model):
    riskname = models.CharField(max_length=50)
    riskid = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self, riskname):
        if type(riskname) is not unicode or riskname == '':
            raise error.RTException(error.RISKTYPE_NAME_EMPTY)
        try:
            rt = RiskType.objects.get(riskname=riskname)
        except RiskType.DoesNotExist:
            self.created_date = timezone.now()
            self.riskname = riskname
            try:
                self.save()
            except Exception as e:
                raise error.RTException(error.RISKTYPE_COULD_NOT_BE_CREATED, 500)
        except Exception as e:
            raise error.RTException(error.RISKTYPE_COULD_NOT_BE_CREATED, 500)
        else:
            raise error.RTException(error.RISKTYPE_EXISTS)

    def getId(self):
        return self.riskid

    def __str__(self):
        return self.riskname

"""RiskTypeAttribute model class"""
class RiskTypeAttribute(models.Model):
    riskattrid = models.AutoField(primary_key=True)
    risktype = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    riskattrname = models.CharField(max_length=50)
    riskattrtype = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self, rt, rattrname, rattrtype):
        if type(rattrname) is not unicode or type(rattrtype) is not unicode or rattrname == '' or rattrtype == '':
            raise error.RTException(error.RISKTYPE_ATTR_INFO_EMPTY)
        if rattrtype not in globals.RT_ATTR_TYPES:
            raise error.RTException(error.RISKTYPE_ATTR_TYPE_INVALID)
        self.created_date = timezone.now()
        self.risktype = rt
        self.riskattrname = rattrname
        self.riskattrtype = rattrtype
        try:
            self.save()
        except Exception as e:
            raise error.RTException(error.RISKTYPE_ATTR_COULD_NOT_BE_CREATED, 500)

    def __str__(self):
        return self.riskattrname

"""RiskTypeAttributeEnumEntry model class"""
class RiskTypeAttributeEnumEntry(models.Model):
    riskattr = models.ForeignKey(RiskTypeAttribute, on_delete=models.CASCADE)
    riskenumentryname = models.CharField(max_length=10)
    riskenumentryvalue = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self, rta, renumentryname, renumentryvalue):
        if type(renumentryname) is not unicode or type(renumentryvalue) is not unicode or renumentryname == '' or renumentryvalue == '':
            raise error.RTException(error.RISKTYPE_ATTR_ENUM_INFO_EMPTY)
        self.created_date = timezone.now()
        self.riskattr = rta
        self.riskenumentryname = renumentryname
        self.riskenumentryvalue = renumentryvalue
        try:
            self.save()
        except Exception as e:
            raise error.RTException(error.RISKTYPE_ATTR_ENUM_ENTRY_COULD_NOT_BE_CREATED, 500)

    def __str__(self):
        return self.riskenumentryname + ' : ' + self.riskenumentryvalue