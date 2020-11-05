from pynput.keyboard import Key, Controller
import pyperclip

class Keybinding:
    def __init__(self):
        self.keyboard = Controller()
        
    def func_name(self, command):
        name = "self.t" + str(command)
        eval(name + '()')
    
    def t0(self, message):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('h')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('h')
        pyperclip.copy(message)
        #pyperclip.paste()
        self.keyboard.press(Key.cmd)
        self.keyboard.press('v')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('v')

    def t1(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def t2(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('w')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('w')

    def t3(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('l')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('l')

    def t4(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('l')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('l')

    def t5(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('t')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('t')

    def t6(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('j')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('j')

    def t7(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('v')

    def t8(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('j')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('j')

    def t9(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('s')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('s')

    def t10(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('a')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('a')

    def t11(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('a')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('a')

    def t12(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('m')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('m')

    def t13(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('u')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('u')

    def t14(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('v')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('v')

    def t15(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('v')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('v')

    def t16(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('n')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('n')

    def t17(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('s')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('s')

    def t18(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('s')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('s')

    def t19(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('t')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('t')

    def t20(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('t')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('t')

    def t21(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('r')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('r')

    def t22(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('c')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('c')

    def t23(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('p')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('p')

    def t24(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('p')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('p')

    def t25(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('w')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('w')

    def t26(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('w')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('w')

    def t27(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('p')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('p')

    def t28(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('n')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('n')

    def t29(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('u')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('u')

    def t30(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('u')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('u')

    def t31(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('h')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('h')

    def t32(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('h')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('h')

    def t33(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('i')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('i')

    def t34(self):
        self.keyboard.press(Key.alt)
        self.keyboard.press('y')
        self.keyboard.release(Key.alt)
        self.keyboard.release('y')

    def t35(self):
        self.keyboard.press(Key.alt)
        self.keyboard.press('y')
        self.keyboard.release(Key.alt)
        self.keyboard.release('y')

    def t36(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('r')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('r')

    def t37(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('g')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('g')

    def t38(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('f')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('f')

    def t39(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('f')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('f')

    def t40(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press('m')
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.keyboard.release('m')

    def t41(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.alt)
        self.keyboard.press(Key.cmd)
        self.keyboard.press('h')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.alt)
        self.keyboard.release(Key.cmd)
        self.keyboard.release('h')

    def t42(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.alt)
        self.keyboard.press(Key.cmd)
        self.keyboard.press('h')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.alt)
        self.keyboard.release(Key.cmd)
        self.keyboard.release('h')

    def t43(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('\\')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('\\')

    def t44(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('w')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('w')

    def t45(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('w')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('w')

    def t46(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('k')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('k')

    def t47(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('t')
        self.keyboard.release(Key.cmd)
        self.keyboard.release('t')

    def t48(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('c')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('c')

    def t49(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('a')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('a')

    def t50(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('d')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('d')

    def t51(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('e')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('e')

    def t52(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('m')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('m')

    def t53(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('m')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('m')

    def t54(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('h')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('h')

    def t55(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('h')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)
        self.keyboard.release('h')