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


# def test_java_installed(host):
#     print("---")
#     print(host.check_output("java -version"))
#     print("---")
#     assert host.check_output("java -version").find("1.8.") > 0


def test_application_folder(host):
    assert host.file("/app/minecraft").exists
