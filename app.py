from bottle import route, run, template,Bottle, static_file, post, request
import re
import six
print six.__file__
#from home_iot import process_name

@route('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')

@route('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')

@route('/css/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='css/images')

@route('/fonts/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='fonts')

@route('/../fonts/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='fonts')

@route('/')
@route('/<filename>')
def static(filename="home.html"):
    return static_file(filename, root='.')

#import sys
#
#
#@route('/hello/<name>')
#def greet(name='Stranger'):
#    #if name.find("music") != -1:
#    #  control_music(name)
#    #elif name.find("tv") != -1:
#    #  control_tv(name)
#    #elif name in ir_codes:
#    #  control_lights(name)
#    #info = {"title":"hello world",'get_url': Bottle.get_url}
#    #process_name(name)
#    return template('Hello {{name}}, how are you?', name=name)
#    #return template("index.tpl", info)
#
#@route('/ajax', method='POST')
#def do_ajax():
#    print vars(request.forms)
#    Cfg.num_pkts = int(request.forms.num_pkts)
#    Cfg.long_flow_perc = int(request.forms.long_flow_perc)
#    Cfg.arb_mode = int(request.forms.arb_mode)
#    if "debug" in request.forms:
#        Cfg.debug = int(request.forms.debug)
#    else:
#        Cfg.debug = False
#    Cfg.long_flow_min = int(request.forms.long_flow_min)
#    Cfg.long_flow_max = int(request.forms.long_flow_max)
#    Cfg.rtc_cnt = int(request.forms.rtc_cnt)
#    Cfg.lkup_latency = int(request.forms.lkup_latency)
#    Cfg.lkup_fifo_depth = int(request.forms.lkup_fifo_depth)
#    rtest = Rtc_Test()
#    return rtest.start()
#    
#@route('/get_r_number', method='GET')
#def do_r_number():
#    return str(Cmn.received_pkts)

run(host="192.168.1.17", port=8000, debug=True, reloader=True)


