#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :Logs lynis-report - HTML
#author          :networkingdayss
#date            :05-09-2018
#version         :0.1 - Beta
#usage           :python lynis_cron_job.py
#notes           :Need some verification ajustments and new features (install lynis and ansi2html)
#python_version  :2.7.5  
#=======================================================================
import sys, os, time, subprocess, six

if __name__ == "__main__":

	auditor = "Cron Job"
	log_dir = "/var/log/"
	
	hostname=subprocess.check_output("hostname", shell=True).strip()
		
	data_auditoria=subprocess.check_output("date +%F_%R", shell=True)
	data_auditoria=data_auditoria.rstrip('\r\n').strip().replace(" ", "_").replace(":", "h")

	email_destino = "your_destiny_email_address"
	
	corpo_email = "Auditoria executada à data de %s, relatório em anexo." %(data_auditoria)
	subject = "Auditoria agendada: %s" % (hostname)
	
	cmd_lynis = "lynis audit system --auditor '%s'| ansi2html -la > audit_report_'%s'_'%s'.html"
	email_cmd = "echo ''%s | mail -s '%s' -a audit_report_'%s'_'%s'.html '%s'"
	
	cmd_test_lynis = subprocess.check_output("type -P lynis || echo $?", shell=True).strip()
	cmd_test_ansi2html = subprocess.check_output("type -P ansi2html || echo $?", shell=True).strip()
	
	fail_mail = "Auditoria agendada para %s não foi executada" % (hostname)
	corpo_fail_email = "O Lynis não conseguiu realizar a auditoria pretendida em: %s." %(data_auditoria)
	email_cmd_fail = "echo ''%s | mail -s '%s' '%s'"
	
	if (cmd_test_lynis == "/bin/lynis" and cmd_test_ansi2html == "/bin/ansi2html"):
		subprocess.check_output(cmd_lynis%(auditor,hostname,data_auditoria),shell=True)
		subprocess.check_output(email_cmd%(corpo_email,subject,hostname,data_auditoria,email_destino),shell=True)
	else:
		subprocess.check_output(email_cmd_fail%(corpo_fail_email,fail_mail,email_destino),shell=True)
		
			

				
			
	