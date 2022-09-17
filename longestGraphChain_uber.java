/*
Given an input of a list of lists, each list contains a list of node_ids. The order of the list [A,B] represents a one way connection from node A to node B, and node_ids that are the same between different lists are the same node.

We want to find the number of nodes in the longest chain across all the input lists.

  

Lets say we are given list -> ["A", "C", "D"], then A connected to C, and C connected to D. This way we will be given list of lists which has several node links, we need to longest connected chain in this.

  

Input:

[["A", "C", "D"],

["A", "B", "E"],

["D", "F", "G", "H"],

["Z", "X", "C", "Q", "R"]]

  

R -> [Q]

Q -> [C]

C -> [A, X]

A -> [F, G, H]

X -> [T, U, V]

  

Solution for longest chain - z, x, c, d, f, g, h

Output: 7

  
  

*/

import java.util.*;


public class Solution {

    public static void main(String[] args) {
        System.out.println("Hello, World");
        List<List<String>> data = new ArrayList<List<String>>();
        List<String> list = new ArrayList<String>();
        list.add("A");
        list.add("C");
        list.add("D");
        data.add(list);
        List<String> list1 = new ArrayList<String>();
        list1.add("A");
        list1.add("B");
        list1.add("E");
        data.add(list1);
        List<String> list2 = new ArrayList<String>();
        list2.add("R");
        list2.add("F");
        list2.add("G");
        list2.add("H");
        data.add(list2);
        List<String> list3 = new ArrayList<String>();
        list3.add("Z");
        list3.add("X");
        list3.add("C");
        list3.add("Q");
        list3.add("R");
        data.add(list3);

        Pair<Map<String, List<String>>, Set<String>> graphData = constructGraph(data);


        Map<String, List<String>> graph = graphData.getFirst();

        Set<String> leafNodes = graphData.getSecond();

        System.out.println(graph);
        System.out.println(leafNodes);

        Map<String, Integer> chainCounts = new HashMap<String, Integer>();

        List<Pair<String, Integer>> nodesToProcess = new ArrayList<Pair<String, Integer>>();

        for (String leafnode : leafNodes) {

            nodesToProcess.add(new Pair<String, Integer>(leafnode, 1));

        }

        int maxChain = 0;

        while (nodesToProcess.size() > 0) {

            Pair<String, Integer> node = nodesToProcess.get(0);

            nodesToProcess.remove(node);

            if (!graph.containsKey(node.getFirst())) continue;

            List<String> parentNodes = graph.get(node.getFirst());

            Integer chainLen = node.getSecond();

            for (String parentNode : parentNodes) {

                updateCount(parentNode, chainLen + 1, chainCounts);

                nodesToProcess.add(new Pair<String, Integer>(parentNode, Integer.valueOf(chainLen + 1)));

            }

            if (chainLen + 1 > maxChain) {

                maxChain = chainLen + 1;

            }

        }

        System.out.println(maxChain);

    }

    public static void updateCount(String node, int newcount, Map<String, Integer> chainCounts) {

        if (!chainCounts.containsKey(node)) {

            chainCounts.put(node, newcount);

        } else {

            if (chainCounts.get(node) < newcount) chainCounts.put(node, newcount);

        }

    }

    public static Pair<Map<String, List<String>>, Set<String>> constructGraph(List<List<String>> data) {

        Map<String, List<String>> graph = new HashMap<String, List<String>>();

        Set<String> leafnodes = new HashSet<String>();

        for (List<String> connects : data) {

            String prevNode = null;

            String currNode = null;

            for (String node : connects) {

                if (leafnodes.contains(node)) {

                    leafnodes.remove(node);

                }

                if (prevNode == null) {

                    prevNode = node;

                } else {

                    updateGraph(graph, prevNode, node);

                    prevNode = node;

                }

            }

            leafnodes.add(prevNode);

        }

        return new Pair(graph, leafnodes);

    }

    public static void updateGraph(Map<String, List<String>> graph, String start, String end) {

        if (!graph.containsKey(end)) {

            graph.put(end, new ArrayList<String>());

        }

        graph.get(end).add(start);

    }

}

final class Pair<type1, type2> {

    private final type1 a;
    private final type2 b;

    public Pair(type1 a, type2 b) {
        this.a = a;
        this.b = b;
    }

    public type1 getFirst() {
        return a;
    }

    public type2 getSecond() {
        return b;
    }
}
