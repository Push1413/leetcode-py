class Solution {
     public static double calculateDistance(int x1, int y1, int x2, int y2) {
        double deltaX = (double)x2 - x1;
        double deltaY = (double)y2 - y1;
        return Math.sqrt(deltaX * deltaX + deltaY * deltaY);
    }
    public int[][] kClosest(int[][] points, int k) {
        int[][]res = new int[k][2];
        int size = points.length;
        if (size<2){
            return points;
        }

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            (p1, p2) -> {
                double dist1 = calculateDistance(p1[0], p1[1], 0, 0);
                double dist2 = calculateDistance(p2[0], p2[1], 0, 0);
                return Double.compare(dist1, dist2);
            }
        );

        for(int[] point:points){
            minHeap.offer(point);
        } 

        for (int i=0;i<k;i++){
            res[i] = minHeap.poll();
        }

        return res;

    }
}