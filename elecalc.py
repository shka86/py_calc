#!/usr/bin/python3
# -*- coding: utf-8 -*-

# calculation tool for a bridge circuit with two input current sources
# two current sources can supply from both of top of the bridge and middle of the bridge
# define the voltage name as follows:
# Vp: voltage at the top of the bridge
# Vn: voltage at the middle of the bridge

def paraR(R1, R2):
    return R1*R2/(R1+R2)

def unbalanced_bridge(  I = 1, Ra = 1, Rb = 1, Rc = 1, Rd = 1, Re = 1, Rf = 1):
    print("# --- calc unbalanced bridge ---------------")
    # params
    print("I=", I, "A")
    print("Ra=", Ra, "ohm")
    print("Rb=", Rb, "ohm")
    print("Rc=", Rc, "ohm")
    print("Rd=", Rd, "ohm")
    print("Re=", Re, "ohm")
    print("Rf=", Rf, "ohm")

    # delta-Y transpose
    denom = Ra + Rb + (Rc + Rd)
    Ralpha = Ra * Rb / denom
    Rbeta = (Rc + Rd) * Ra / denom
    Rgamma = Rb * (Rc + Rd) / denom

    print("denom=", denom, "ohm")
    print("Ralpha=", Ralpha, "ohm")
    print("Rbeta=", Rbeta, "ohm")
    print("Rgamma=", Rgamma, "ohm")

    # I sprit
    Il = (Rgamma + Rf) / ((Rbeta + Re) + (Rgamma + Rf)) * I
    Ir = (Rbeta + Re) / ((Rbeta + Re) + (Rgamma + Rf)) * I
    print("Il=", Il, "A")
    print("Ir=", Ir, "A")

    # calc Vtop and Vmid
    Vl = Re * Il
    Vr = Rf * Ir
    print("Vl=", Vl, "V")
    print("Vr=", Vr, "V")

    Vtop = (Ralpha + (paraR((Rbeta + Re), (Rgamma + Rf)))) * I
    Vmid = (Rd * Vl + Rc * Vr) / (Rc + Rd)

    print("Vtop=", Vtop, "V")
    print("Vmid=", Vmid, "V")

    return Vtop, Vmid

def main():

    # current of two input sources
    current1 = 2.5e-3
    current2 = 1.25e-3

    # unbaranced brigde params
    # branch on input side
    Ra = 100
    Rb = 100
    # bridge part (series resistor)
    Rc = 100
    Rd = 100
    # branch on ground side
    Re = 50
    Rf = 50

    current1 = 2
    current2 = 1
    Vtop1, Vmid1 = unbalanced_bridge(current1, Ra, Rb, Rc, Rd, Re, Rf)
    Vtop2, Vmid2 = unbalanced_bridge(current2, Ra, Rb, Rc, Rd, Re, Rf)

    print("# --- sum based on superposition theorem ---------------")
    print("# when two current sources supply from top")
    Vp = Vtop1 + Vtop2
    Vn = Vmid1 + Vmid2
    print("Vp=", Vp, "V")
    print("Vn=", Vn, "V")

    # same meaning
    # unbalanced_bridge(current1+current2, Ra, Rb, Rc, Rd, Re, Rf)
 
    print("# when current1 from the top, current2 from the middle")
    Vp = Vtop1 + Vmid2
    Vn = Vmid1 + Vtop2
    print("Vp=", Vp, "V")
    print("Vn=", Vn, "V")

    print("# when current2 from the top, current1 from the middle")
    Vp = Vmid1 + Vtop2
    Vn = Vtop1 + Vmid2
    print("Vp=", Vp, "V")
    print("Vn=", Vn, "V")

    print("# when two current sources from middle")
    Vp = Vmid1 + Vmid2
    Vn = Vtop1 + Vtop2
    print("Vp=", Vp, "V")
    print("Vn=", Vn, "V")

if __name__ == '__main__':

    main()
