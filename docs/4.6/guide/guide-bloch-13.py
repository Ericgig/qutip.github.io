xz = np.zeros(20)
yz = np.sin(th)
zz = np.cos(th)

b.add_points([xz, yz, zz])  # no 'm'
b.render()