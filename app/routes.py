from app import app
from flask import url_for, render_template, request, jsonify
from nornir import InitNornir

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('views/dashboard.html')


@app.route('/inventory')
def inventory():

    return render_template('views/inventory.html')

@app.route('/api/inventory')
def ajax_inventory():
    nr = InitNornir(config_file="app/config.yaml")
    data = []

    for host in nr.inventory.hosts:
        host_dict = nr.inventory.hosts[host].dict()
        device_data = [
            host_dict["name"],
            host_dict["hostname"],
            host_dict["platform"],
            host_dict["data"]["role"],
            ",".join(host_dict["groups"])
        ]
        data.append(device_data)

    return jsonify({"data":data})

@app.route('/config-management')
def config_management():
    return render_template('views/config-management.html')
