import js2py

js = '''var calculateNUSMatricNumber = function (id) {
          var matches = id.toUpperCase().match(/^A\d{7}|U\d{6,7}/);
          if (matches) {
              var match = matches[0];

              // Discard 3rd digit from U-prefixed NUSNET ID
              if (match[0] === 'U' && match.length === 8) {
                  match = match.slice(0, 3) + match.slice(4);
              }

              var weights = {
                  U: [0, 1, 3, 1, 2, 7],
                  A: [1, 1, 1, 1, 1, 1]
              }[match[0]];

              for (var i = 0, sum = 0, digits = match.slice(-6); i < 6; i++) {
                  sum += weights[i] * digits[i];
              }

              return match + 'YXWURNMLJHEAB'[sum % 13];
          }
      };
    '''

##A0171424M/077L_DSC_3683.jpg

calculate = js2py.eval_js(js)

def A():
    for num in range(1, 10000000):
        front = "A" + str(num).zfill(7)
        full = calculate(front)
        print(full)
        with open('nusnetidA.txt','a',encoding='utf-8') as f:
            f.write(full)
            f.write('\n')

def U():
    for num in range(1, 10000000):
        front = "U" + str(num).zfill(7)
        full = calculate(front)
        print(full)
        with open('nusnetidU.txt','a',encoding='utf-8') as f:
            f.write(full)
            f.write('\n')

A()
U()
