#!/bin/bash

JVM_OPTS="${JVM_OPTS} -Xms{{ minecraft_java_min_ram }} -Xmx{{ minecraft_java_max_ram }}"
APP_OPTS="${APP_OPTS} nogui"

java ${JVM_OPTS} -jar {{ minecraft_install_folder }}/server.jar ${APP_OPTS}
