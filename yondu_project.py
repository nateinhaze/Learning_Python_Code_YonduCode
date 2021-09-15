'''
Project Name: Yundu Project
Author: Nathan Warnick
Due Date: 09/18/2021
Course: CS1400

I learned a lot about how a program layout is supposed to be in Python, I practiced mathmatics logic in this program.
'''

def main():
    '''
    Program starts here.
    
    '''
    try:
        reavers = int(input('enter reavers number: '))
        units = int(input('enter units number: '))
        
    except ValueError:
        print("Enter postive integers for reavers and units.")
        return
    
    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return
    
    #my code starts here:
    
  
    celebration = (reavers * 3)
    celebration = (celebration - 6)
    units_afterc = (units - celebration)
    yondu_b = 0
    yondu_b = int(units_afterc * 0.13)
    units_now = (units_afterc - yondu_b)
    quill_b = 0
    quill_b = int(units_now * 0.11)
    units_now = (units_now - quill_b)
    RBF = (units_now % reavers)
    final_amount = int(units_now - RBF)
    crew = int(final_amount / reavers)
    yondu_b = (yondu_b + crew)
    quill_b = (quill_b + crew)
    
    print("How many Reavers:")
    print(reavers)
    print("How many units:")
    print(units)
    print("Yondu's share:",yondu_b)
    print("Peter's share:",quill_b)
    print("Crew:",crew)
    print("RBF:",RBF)
    
    #my code ends here!
if __name__ == "__main__":
    main()
    

