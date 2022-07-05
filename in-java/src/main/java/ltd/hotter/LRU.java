package ltd.hotter;

import java.util.HashMap;
import java.util.Map;

class LRUCache {
    int capacity;
    int size;
    LruNode head;
    LruNode tail;
    Map<Integer ,LruNode> map;

    public LRUCache(int capacity) {
        this.capacity=capacity;
        this.size=0;
        map=new HashMap<>(capacity);
        head=new LruNode();
        tail=new LruNode();
        head.next=tail;
        tail.pre=head;
    }
    
    public int get(int key) {
        LruNode node= map.get(key);
        if(node==null){
            return -1;
        }
        moveToHead(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        LruNode node= map.get(key);
        if(node==null){
            node=new LruNode(key,value);
            addToHead(node);
            map.put(key,node);
            ++size;
            if(size>capacity){
                LruNode tail= removeTail();
                map.remove(tail.key);
                --size;
            }
        }else{
            node.value=value;
            moveToHead(node);
        }
    }

    private void moveToHead(LruNode node){
        remove(node);
        addToHead(node);
    }

    private void remove(LruNode node){
        node.next.pre=node.pre;
        node.pre.next=node.next;

    }

    private void addToHead(LruNode node){
        node.next=head.next;
        node.next.pre=node;
        head.next=node;
        node.pre=head;
    }

    private LruNode removeTail(){
            LruNode pre=tail.pre;
            remove(pre);
            return pre;
    }

    class LruNode{
        int key;
        int value;
        LruNode pre;
        LruNode next;

        public LruNode(){

        }

        public LruNode(int key,int value){
            this.key=key;
            this.value=value;
        }
    } 

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
