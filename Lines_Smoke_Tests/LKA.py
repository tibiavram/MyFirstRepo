from Main import wb,exported_xlsx,filter_different_to_or ,filter_lower_than, filter_higher_than, filter_equal_to, filter_different_to, filter_lower_than_or, filter_higher_than_or, filter_not_same_sign

# SysTs_LKA_LPA_DAA_202
ws202 = wb.copy_worksheet (wb.active)
ws202.title = "SysTs_LKA_LPA_DAA_202"

filter_lower_than(ws202,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws202,"VITESSE_VEHICULE_ROUES",180)

filter_different_to_or(ws202,"RIGHT_LINE_TYPE_EXT","LEFT_LINE_TYPE_EXT",1)

filter_lower_than_or(ws202,"LANE_MARK_QUALITY_LEFT","LANE_MARK_QUALITY_RIGHT",2)


# SysTs_LKA_LPA_DAA_204
ws204 = wb.copy_worksheet (wb.active)
ws204.title = "SysTs_LKA_LPA_DAA_204"

filter_lower_than(ws204,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws204,"VITESSE_VEHICULE_ROUES",180)

filter_different_to_or(ws204,"SEC_LEFT_LINE_TYPE_EXT","SEC_RIGHT_LINE_TYPE_EXT",1)

filter_lower_than_or(ws204,"LANE_MARK_QUALITY_NL","LANE_MARK_QUALITY_NR",2)

# SysTs_LKA_LPA_DAA_205
ws205 = wb.copy_worksheet (wb.active)
ws205.title = "SysTs_LKA_LPA_DAA_205"

filter_lower_than(ws205,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws205,"VITESSE_VEHICULE_ROUES",180)

filter_different_to_or(ws205,"RIGHT_LINE_TYPE_EXT","LEFT_LINE_TYPE_EXT",2)

filter_lower_than_or(ws205,"LANE_MARK_QUALITY_LEFT","LANE_MARK_QUALITY_RIGHT",2)

# SysTs_LKA_LPA_DAA_206
ws206 = wb.copy_worksheet (wb.active)
ws206.title = "SysTs_LKA_LPA_DAA_206"

filter_lower_than(ws206,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws206,"VITESSE_VEHICULE_ROUES",180)

filter_different_to_or(ws206,"SEC_LEFT_LINE_TYPE_EXT","SEC_RIGHT_LINE_TYPE_EXT",2)

filter_lower_than_or(ws206,"LANE_MARK_QUALITY_NL","LANE_MARK_QUALITY_NR",2)

# SysTs_LKA_LPA_DAA_229
ws229 = wb.copy_worksheet (wb.active)
ws229.title = "SysTs_LKA_LPA_DAA_229"

filter_lower_than(ws229,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws229,"VITESSE_VEHICULE_ROUES",180)

filter_different_to_or(ws229,"RIGHT_LINE_TYPE_EXT","LEFT_LINE_TYPE_EXT",5)

filter_lower_than_or(ws229,"LANE_MARK_QUALITY_LEFT","LANE_MARK_QUALITY_RIGHT",2)

# SysTs_LKA_LPA_DAA_230
ws230 = wb.copy_worksheet (wb.active)
ws230.title = "SysTs_LKA_LPA_DAA_230"

filter_lower_than(ws230,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws230,"VITESSE_VEHICULE_ROUES",180)

filter_different_to_or(ws230,"RIGHT_LINE_TYPE_EXT","LEFT_LINE_TYPE_EXT",6)

filter_lower_than_or(ws230,"LANE_MARK_QUALITY_LEFT","LANE_MARK_QUALITY_RIGHT",2)



wb.save(exported_xlsx)


