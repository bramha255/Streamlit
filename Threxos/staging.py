
led = 4


def create_but(var, i):
    var = st.radio(label=var, key=(np.random.random()),
                   options=('On', 'Off'), horizontal=True)


for i in range(1, led+1):
    var = 'LED'+str(i)
    create_but(var, i)
var, i
