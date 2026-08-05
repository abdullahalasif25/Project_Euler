def number_letters_count(limit):

    def num_to_words(num):
        ones = ["", "one", "two", "three", "four", "five", "six", "seven",  "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 'sixteen', "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        
        def below_one_hundred(num):
            if 1 <= num <= 9:
                return ones[num]
            elif 10 <= num <= 19:
                return teens[num%10]
            elif 20 <= num <= 99:
                if num%10 == 0:
                    return tens[num//10]
                else:
                    return tens[num//10] + "-" + ones[num%10]


        if 1 <= num <= 99:
            return below_one_hundred(num)
        
        words = ""       
        if 100 <= num <=999:
            words += ones[num//100] + " hundred"
            if num%100 != 0:
                words += " and " + below_one_hundred(num%100)
                return words
            else:
                return words
        if num == 1000:
                return "one thousand"
            

    def word_count(number):
        z= num_to_words(number)
        return (len(z) - z.count(" ") - z.count("-"))

    total = 0
    for i in range(1, limit + 1):
        total += word_count(i)
    return total
        
print(number_letters_count(1000))