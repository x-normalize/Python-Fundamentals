from math import floor

the_biscuits_for_day_per_one_worker = int(input())
the_counts_for_workers = int(input())
the_competing_factory_biscuits_for_a_month = int(input())
the_total_biscuits_for_all_day = the_biscuits_for_day_per_one_worker * the_counts_for_workers
total_days = 30
the_total = 0

for the_day in range(1, total_days + 1):
    the_total += the_total_biscuits_for_all_day

    if the_day % 3 == 0:
        the_total -= the_total_biscuits_for_all_day * 0.25
        the_total = floor(the_total)

print(f'You have produced {the_total} biscuits for the past month.')

if the_total > the_competing_factory_biscuits_for_a_month:
    difference = the_total - the_competing_factory_biscuits_for_a_month
    percentage = difference / the_competing_factory_biscuits_for_a_month * 100
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    difference = the_competing_factory_biscuits_for_a_month - the_total
    percentage = difference / the_competing_factory_biscuits_for_a_month * 100
    print(f'You produce {percentage:.2f} percent less biscuits.')
