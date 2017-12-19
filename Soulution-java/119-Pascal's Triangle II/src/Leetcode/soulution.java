package Leetcode;

/**
 * Created by hj on 16-9-6.
 */
public class solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> list = new ArrayList<Integer> (rowIndex + 1);
        list.add(1);

        if (rowIndex == 0) {
            return list;
        }

        list.add(1);
        if (rowIndex == 1) {
            return list;
        }

        for (int i = 2; i <= rowIndex; ++i) {
            list.add(1);
            for (int j = i - 1; j > 0; --j) {
                list.set(j, list.get(j) + list.get(j - 1));
            }
        }
        return list;
    }
}