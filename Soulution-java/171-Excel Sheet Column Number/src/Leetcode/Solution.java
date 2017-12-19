package Leetcode;

/**
 * Created by hj on 16-8-9.
 * Related to question Excel Sheet Column Title

    Given a column title as appear in an Excel sheet,
    return its corresponding column number.
 */
public class Solution
{
    // 26进制数
    public int titleToNumber(String s)
    {
        int result = 0;
        for(int i=s.length()-1;i>=0;i--)
        {
            // ASCii
            //System.out.println(s.charAt(i));
            result += (Integer.valueOf(s.charAt(i))-64)*Math.pow(26,s.length()-1-i);
        }
        //System.out.println(result);
        return result;
    }
}
