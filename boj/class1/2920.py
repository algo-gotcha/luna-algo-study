scale = list(map(int, input().split()))

sorted_scale = sorted(scale)


if scale[0] < scale[1]:
	sorted_scale = sorted(scale)
	if scale != sorted_scale:
		print("mixed")
	else:
		print("ascending")
else:
	sorted_scale = sorted(scale, reverse=True)
	if scale != sorted_scale:
		print("mixed")
	else:
		print("descending")


# slower but cleaner

#scale = list(map(int, input().split()))

#sorted_scale = sorted(scale)


#if scale == sorted(scale):
#	print("ascending")
#elif scale == sorted(scale, reverse=True):
#	print("descending")
#else:
#	print("mixed")

