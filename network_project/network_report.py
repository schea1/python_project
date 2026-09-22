# network_report.py

def get_devices():
    # Return a list of device dictionaries
    devices = [
        {
            "hostname": "core-sw1",
            "device_type": "switch",
            "mgmt_ip": "10.0.0.1",
            "location": "Data Center",
            "status": "up",
            "cpu": 35,
            "memory": 50,
            "uptime_days": 120,
            "backup_status": "success"
        },
        {
            "hostname": "core-sw2",
            "device_type": "switch",
            "mgmt_ip": "10.0.0.2",
            "location": "Data Center",
            "status": "up",
            "cpu": 80,
            "memory": 70,
            "uptime_days": 5,
            "backup_status": "failed"
        },
        {
            "hostname": "edge-rtr1",
            "device_type": "router",
            "mgmt_ip": "192.168.1.1",
            "location": "Branch A",
            "status": "down",
            "cpu": 10,
            "memory": 20,
            "uptime_days": 0,
            "backup_status": "failed"
        },
        {
            "hostname": "edge-rtr2",
            "device_type": "router",
            "mgmt_ip": "192.168.2.1",
            "location": "Branch B",
            "status": "up",
            "cpu": 90,
            "memory": 85,
            "uptime_days": 2,
            "backup_status": "success"
        },
        {
            "hostname": "ap-01",
            "device_type": "access-point",
            "mgmt_ip": "10.10.10.11",
            "location": "Office Floor 1",
            "status": "up",
            "cpu": 40,
            "memory": 60,
            "uptime_days": 30,
            "backup_status": "success"
        },
        {
            "hostname": "ap-02",
            "device_type": "access-point",
            "mgmt_ip": "10.10.10.12",
            "location": "Office Floor 2",
            "status": "up",
            "cpu": 75,
            "memory": 90,
            "uptime_days": 1,
            "backup_status": "success"
        },
        {
            "hostname": "fw-01",
            "device_type": "firewall",
            "mgmt_ip": "172.16.0.1",
            "location": "Data Center",
            "status": "up",
            "cpu": 95,
            "memory": 92,
            "uptime_days": 200,
            "backup_status": "success"
        },
        {
            "hostname": "fw-02",
            "device_type": "firewall",
            "mgmt_ip": "172.16.0.2",
            "location": "DR Site",
            "status": "up",
            "cpu": 20,
            "memory": 30,
            "uptime_days": 10,
            "backup_status": "failed"
        }
    ]
    return devices
