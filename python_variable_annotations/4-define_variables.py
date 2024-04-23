#!/usr/bin/env python3
"""
This module defines and annotates variables with specific values.
"""

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"

if __name__ == "__main__":
    a_var = __import__('4-define_variables').a
    pi_var = __import__('4-define_variables').pi
    bool_var = __import__('4-define_variables').i_understand_annotations
    school_var = __import__('4-define_variables').school

    print(f"a is a {type(a_var)} with a value of {a_var}")
    print(f"pi is a {type(pi_var)} with a value of {pi_var}")
    print(("i_understand_annotations is a "
           f"{type(bool_var)} with a value of {bool_var}"))
    print(f"school is a {type(school_var)} with a value of {school_var}")
