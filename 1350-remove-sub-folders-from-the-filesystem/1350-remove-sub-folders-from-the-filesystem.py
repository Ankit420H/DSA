class Solution:
  def removeSubfolders(self, folder: list[str]) -> list[str]:
    ans = []
    prev = ""

    folder.sort()

    for f in folder:
      if prev and f.startswith(prev) and f[len(prev)] == '/':
        continue
      ans.append(f)
      prev = f

    return ans
