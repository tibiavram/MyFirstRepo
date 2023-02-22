from Main import wb,exported_xlsx,filter_lower_than, filter_higher_than, filter_equal_to, filter_different_to, filter_lower_than_or, filter_higher_than_or, filter_not_same_sign

# SysTs_HPP_299
ws299 = wb.copy_worksheet (wb.active)
ws299.title = "SysTs_HPP_299"

filter_lower_than(ws299,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws299,"VITESSE_VEHICULE_ROUES",180)

filter_lower_than(ws299,"HPP_C0_COEF",-10)
filter_higher_than(ws299,"HPP_C0_COEF",10)

filter_equal_to(ws299,"HPP_CONF_MEASURE",0)

# SysTs_HPP_301
ws301 = wb.copy_worksheet (wb.active)
ws301.title = "SysTs_HPP_301"

filter_lower_than(ws301,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws301,"VITESSE_VEHICULE_ROUES",180)

filter_lower_than(ws301,"HPP_C1_COEF",-30)
filter_higher_than(ws301,"HPP_C1_COEF",30)

filter_not_same_sign(ws301,"HPP_C1_COEF","HEADING_ANGLE_LEFT_LINE")
filter_not_same_sign(ws301,"HPP_C1_COEF","HEADING_ANGLE_RIGHT_LINE")

filter_equal_to(ws301,"HPP_CONF_MEASURE",0)


# SysTs_HPP_302
ws302 = wb.copy_worksheet (wb.active)
ws302.title = "SysTs_HPP_302"

filter_lower_than(ws302,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws302,"VITESSE_VEHICULE_ROUES",180)


filter_lower_than(ws302,"HPP_C2_COEF",-0.05)
filter_higher_than(ws302,"HPP_C2_COEF",0.05)


filter_equal_to(ws302,"HPP_CONF_MEASURE",0)


# SysTs_HPP_303
ws303 = wb.copy_worksheet (wb.active)
ws303.title = "SysTs_HPP_303"

filter_lower_than(ws303,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws303,"VITESSE_VEHICULE_ROUES",180)


filter_lower_than(ws303,"HPP_C3_COEF",-0.00012)
filter_higher_than(ws303,"HPP_C3_COEF",0.00012)


filter_equal_to(ws303,"HPP_CONF_MEASURE",0)

wb.save(exported_xlsx)