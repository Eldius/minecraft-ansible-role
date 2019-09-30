import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_service_user(host):
    u = host.user("minecrafter")
    assert u.exists


def test_application_folder(host):
    assert host.file("/app/minecraft").exists


def test_service_file(host):
    assert host.file(
        '/etc/systemd/system/minecraft.service'
        ).contains(
            "ExecStart=/app/minecraft/bedrock_server"
            ) > 0
    assert host.file(
        '/etc/systemd/system/minecraft.service'
        ).contains(
            "Environment=LD_LIBRARY_PATH=/app/minecraft"
            ) > 0
