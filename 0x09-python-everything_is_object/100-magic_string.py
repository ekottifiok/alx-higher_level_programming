#!/usr/bin/python3

def magic_string(persistent_dict={'a': 1}):
    m_string = ""
    m_string += "BestSchool, "*(persistent_dict['a']-1)
    m_string += "BestSchool"
    persistent_dict['a'] += 1
    return m_string
