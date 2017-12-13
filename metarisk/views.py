# metarisks/views.py
import json
from metarisk import error
from metarisk import globals
from metarisk.models import RiskType, RiskTypeAttribute, RiskTypeAttributeEnumEntry
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def createrisktype(request):
    try:
        json_str = ((request.body).decode('utf-8'))
        py_dict = json.loads(json_str)
    except Exception as e:
        raise error.RTException(error.RISKTYPE_CONTENT_DECODE_ERROR, 500)
    if py_dict is None:
        raise error.RTException(error.RISKTYPE_CONTENT_ERROR, 500)
    if type(py_dict) is not dict or globals.RT_NAME not in py_dict or globals.RT_ATTRS not in py_dict or type(py_dict[globals.RT_ATTRS]) is not list or len(py_dict[globals.RT_ATTRS]) == 0:
        raise error.RTException(error.RISKTYPE_CONTENT_ERROR, 500)
    rt = RiskType()
    rt.create(py_dict[globals.RT_NAME])
    for e in py_dict[globals.RT_ATTRS]:
        if type(e) is not dict:
            continue
        if globals.RT_ATTR_NAME not in e or globals.RT_ATTR_TYPE not in e:
            continue
        if e[globals.RT_ATTR_TYPE] == globals.TENUM and (globals.EDICT not in e or type(e[globals.EDICT]) is not dict or len(e[globals.EDICT]) == 0):
            continue
        rta = RiskTypeAttribute()
        try:
            rta.create(rt, e[globals.RT_ATTR_NAME], e[globals.RT_ATTR_TYPE])
            if e[globals.RT_ATTR_TYPE] == globals.TENUM:
                for k in list(e[globals.EDICT].keys()):
                    rtaee = RiskTypeAttributeEnumEntry()
                    rtaee.create(rta, k, e[globals.EDICT][k])
        except Exception as e:
            rt.delete()
            raise e
    r = HttpResponse(content=json.dumps({globals.MSG: error.OK}), content_type='application/json')
    r.status_code = 200
    return r

def getrisktype(rtname):
    try:
        rt = RiskType.objects.get(riskname=rtname)
    except RiskType.DoesNotExist:
        raise error.RTException(error.RISKTYPE_NOT_EXISTS)
    py_dict = {}
    py_dict[globals.RT_NAME] = rt.riskname
    py_dict[globals.RT_ATTRS] = []
    rtaqs = RiskTypeAttribute.objects.filter(risktype=rt)
    for e in rtaqs:
        eed = {}
        if e.riskattrtype == globals.TENUM:
            rtaee = RiskTypeAttributeEnumEntry.objects.filter(riskattr=e)
            for ee in rtaee:
                eed[ee.riskenumentryname] = ee.riskenumentryvalue
            py_dict[globals.RT_ATTRS].append({globals.RT_ATTR_NAME: e.riskattrname, globals.RT_ATTR_TYPE: e.riskattrtype, globals.EDICT : eed})
        else:
            py_dict[globals.RT_ATTRS].append({globals.RT_ATTR_NAME: e.riskattrname, globals.RT_ATTR_TYPE: e.riskattrtype})
    r = HttpResponse(content=json.dumps(py_dict), content_type='application/json')
    r.status_code = 200
    return r

def getrisktypes():
    rtqs = RiskType.objects.all()
    rtl = []
    for e in rtqs:
        py_dict = {}
        py_dict[globals.RT_NAME] = e.riskname
        py_dict[globals.RT_ATTRS] = []
        rtaqs = RiskTypeAttribute.objects.filter(risktype=e)
        for a in rtaqs:
            eed = {}
            if a.riskattrtype == globals.TENUM:
                rtaee = RiskTypeAttributeEnumEntry.objects.filter(riskattr=a)
                for ee in rtaee:
                    eed[ee.riskenumentryname] = ee.riskenumentryvalue
                py_dict[globals.RT_ATTRS].append({globals.RT_ATTR_NAME: a.riskattrname, globals.RT_ATTR_TYPE: a.riskattrtype, globals.EDICT: eed})
            else:
                py_dict[globals.RT_ATTRS].append({globals.RT_ATTR_NAME: a.riskattrname, globals.RT_ATTR_TYPE: a.riskattrtype})
        rtl.append(py_dict)
    r = HttpResponse(content=json.dumps(rtl), content_type='application/json')
    r.status_code = 200
    return r

@csrf_exempt
def risktype(request, rtname=''):
    if request.method == 'POST':
        try:
            return createrisktype(request)
        except Exception as e:
            if type(e) is error.RTException:
                return error.handle_RT_exception(e)
            else:
                return error.handle_RT_exception(error.RTException(e.__str__(), 500))
    elif request.method == 'GET':
        try:
            return getrisktype(rtname)
        except Exception as e:
            if type(e) is error.RTException:
                return error.handle_RT_exception(e)
            else:
                return error.handle_RT_exception(error.RTException(e.__str__(), 500))
    else:
        r = HttpResponse(content=json.dumps({globals.MSG : error.HTTP_METHOD_NOT_SUPPORTED}), content_type='application/json')
        r.status_code = 400
        return r

@csrf_exempt
def risktypes(request):
    if request.method == 'GET':
        try:
            return getrisktypes()
        except Exception as e:
            if type(e) is error.RTException:
                return error.handle_RT_exception(e)
            else:
                return error.handle_RT_exception(error.RTException(e.__str__(), 500))
    else:
        r = HttpResponse(content=json.dumps({globals.MSG : error.HTTP_METHOD_NOT_SUPPORTED}), content_type='application/json')
        r.status_code = 400
        return r

@csrf_exempt
def riskhome(request):
    if request.method == 'GET':
        return render(request, 'risk.htm')
    else:
        r = HttpResponse(content=json.dumps({globals.MSG: error.HTTP_METHOD_NOT_SUPPORTED}),
                         content_type='application/json')
        r.status_code = 400
        return r
