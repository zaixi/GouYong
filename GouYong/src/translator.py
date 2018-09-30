#!/usr/bin/python3.5
#-*- coding:utf-8 -*-

from GouYong.src.google import GoogleTranslate
from GouYong.src.sogou import SogouTranslate
from GouYong.src.youdao import YoudaoTranslate

class Translator(object):
    def __init__(self,  engine = 'google'):
        self.translators = []
        self.translators.append(GoogleTranslate())
        self.translators.append(SogouTranslate())
        self.translators.append(YoudaoTranslate())
        self.set_translator(engine)

    def set_translator(self, engine):
        for translator in self.translators:
            if engine == translator.engine:
                self.translator = translator

    def translate(self, text):
        try:
            result = self.translator.translate(text)
            if text == result:
                for translator in self.translators:
                    result = translator.translate(text)
                    if result != text:
                        break;
            return result
        except:
            return text

    def test(self):
        texts = []
        texts.append("makes control reaches end of non-void functionv")
        texts.append("apple")
        texts.append("translate")
        texts.append("GPIO_DIRECTION_OUTPUT")
        translator = self.translator
        for who in self.translators:
            self.set_translator(who.engine)
            print("\n-----------------", self.translator.engine, "-------------------\n")
            for text in texts:
                result = self.translate(text)
                print(result)

if __name__ == '__main__':
    translator = Translator()
    translator.test()

