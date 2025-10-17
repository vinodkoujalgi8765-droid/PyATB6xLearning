expected_title = "Dashboard"
actual_title = "Dashboard "

if expected_title.strip().lower() == actual_title.strip().lower():
    print("✅ Test Passed – Title matches")
else:
    print("Test failed, it is not the expected title")

