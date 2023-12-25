from nepali_unicode_converter.convert import Converter
converter = Converter()
mystring = 'khaajaa khaana jaane?, khai ke jaanu, kurai mildaina, baru dherai tanaab line dine kaam nagarau na hai ?'

converted_text = converter.convert(mystring)

print(converted_text)