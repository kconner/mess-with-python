import beeptest.booptest

beeptest.booptest.beep()

message = "hello, world"
count = 3
# This fails at runtime. Four ways to find out:
# - Set Type Checking Mode to strict in Python Analysis settings; see squiggles
# - ⇧↩︎, Python: Run Selection/Line in Python Terminal
# - Exception in debugger
# - Exception in console
cat = message + count
print(cat)

# %%
print("A code cell")
