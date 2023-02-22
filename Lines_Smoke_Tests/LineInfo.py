from Main import wb,exported_xlsx,filter_lower_than, filter_higher_than, filter_equal_to, filter_different_to, filter_lower_than_or, filter_higher_than_or, filter_not_same_sign

# SysTs_LineInfo_303
ws303 = wb.copy_worksheet (wb.active)
ws303.title = "SysTs_LineInfo_303"

filter_lower_than(ws303,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws303,"VITESSE_VEHICULE_ROUES",180)

filter_lower_than(ws303,"LANE_MARK_QUALITY_LEFT",2)
filter_lower_than(ws303,"LANE_MARK_QUALITY_RIGHT",2)

filter_equal_to(ws303, "DIST_VHL_L_LINE_EXT",0)
filter_equal_to(ws303, "DIST_VHL_R_LINE_EXT",0)
filter_equal_to(ws303, "HEADING_ANGLE_LEFT_LINE",0)
filter_equal_to(ws303, "HEADING_ANGLE_RIGHT_LINE",0)
filter_equal_to(ws303, "ESTIMATED_CURV_LEFT_LINE",0)
filter_equal_to(ws303, "ESTIMATED_CURV_RIGHT_LINE",0)
filter_equal_to(ws303, "CURV_DERIVATIVE_LEFT_LINE",0)
filter_equal_to(ws303, "CURV_DERIVATIVE_RIGHT_LINE",0)

# SysTs_LineInfo_371
ws371 = wb.copy_worksheet (wb.active)
ws371.title = "SysTs_LineInfo_371"

filter_lower_than(ws371,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws371,"VITESSE_VEHICULE_ROUES",180)

filter_lower_than(ws371,"LANE_MARK_QUALITY_LEFT",2)
filter_lower_than(ws371,"LANE_MARK_QUALITY_RIGHT",2)

filter_equal_to(ws371, "DIST_VHL_L_LINE_EXT",0)
filter_equal_to(ws371, "DIST_VHL_R_LINE_EXT",0)
filter_equal_to(ws371, "HEADING_ANGLE_LEFT_LINE",0)
filter_equal_to(ws371, "HEADING_ANGLE_RIGHT_LINE",0)
filter_equal_to(ws371, "ESTIMATED_CURV_LEFT_LINE",0)
filter_equal_to(ws371, "ESTIMATED_CURV_RIGHT_LINE",0)
filter_equal_to(ws371, "CURV_DERIVATIVE_LEFT_LINE",0)
filter_equal_to(ws371, "CURV_DERIVATIVE_RIGHT_LINE",0)
# to be completed
filter_higher_than(ws371,"CIN_Vehicle_Yaw",10)
filter_lower_than(ws371,"CIN_Vehicle_Yaw",-10)

# SysTs_LineInfo_304
ws304 = wb.copy_worksheet (wb.active)
ws304.title = "SysTs_LineInfo_304"

filter_lower_than(ws304,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws304,"VITESSE_VEHICULE_ROUES",180)

filter_lower_than(ws304,"LANE_MARK_QUALITY_LEFT",2)
filter_lower_than(ws304,"LANE_MARK_QUALITY_RIGHT",2)

filter_equal_to(ws304, "DIST_VHL_L_LINE_EXT",0)
filter_equal_to(ws304, "DIST_VHL_R_LINE_EXT",0)
filter_equal_to(ws304, "HEADING_ANGLE_NL",0)
filter_equal_to(ws304, "HEADING_ANGLE_NR",0)
filter_equal_to(ws304, "EST_CURV_NL",0)
filter_equal_to(ws304, "EST_CURV_NR",0)
filter_equal_to(ws304, "CURV_DERIV_L_NL",0)
filter_equal_to(ws304, "CURV_DERIV_L_NR",0)

# SysTs_LineInfo_306
ws306 = wb.copy_worksheet (wb.active)
ws306.title = "SysTs_LineInfo_306"

filter_lower_than(ws306,"VITESSE_VEHICULE_ROUES",5)
filter_higher_than(ws306,"VITESSE_VEHICULE_ROUES",180)

filter_lower_than(ws306,"LANE_MARK_QUALITY_LEFT",2)
filter_lower_than(ws306,"LANE_MARK_QUALITY_RIGHT",2)

filter_equal_to(ws306, "LANE_MARK_COLOR_LEFT",1)
filter_equal_to(ws306, "LANE_MARK_COLOR_RIGHT",1)
filter_equal_to(ws306, "LANE_MARK_COLOR_NL",1)
filter_equal_to(ws306, "LANE_MARK_COLOR_NR",1)

wb.save(exported_xlsx)
