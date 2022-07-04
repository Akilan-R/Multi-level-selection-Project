ptimum_value_list_for_k_value

xpoints = [100 , 200 ,300, 400, 500, 600, 700, 800 900]

ypoints = np.array(optimum_value_list_for_k_value)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
plt.plot(xpoints,ypoints)
for ij in zip(xpoints,ypoints):
    ax.annotate('(%s, %s)' % ij, xy=ij, textcoords='data') # <--
ax.grid()
plt.show()
plt.savefig("pop_size_vs_optimum.jpg")

