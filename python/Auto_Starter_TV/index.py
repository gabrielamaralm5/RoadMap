from selenium import webdriver

driver = webdriver.Chrome("caminho_para_o_seu_driver")
driver.get("URL_da_pagina")

botao = driver.find_element_by_id("id_do_botao")
botao.click()
