#include <bits/stdc++.h>
using namespace std;
#define INF LLONG_MAX

struct segtree {
    vector<long long> tree;
    int size;
    segtree (int size) {
        int p2 = 1;
        while (p2 < size) {
            p2 *= 2;
        }
        this -> size = p2;
        tree.resize (p2*2, INF);
    }
    void update(int pos, long long val) {
        update (pos,val, 0, 0, size);
    }
    void update(int pos, long long val, int i, int lb, int rb) {
        if ( rb - lb == 1){
            tree[i] = val;
            return;
        }
        int mid = (lb + rb) / 2;
        if ( pos < mid ){
            update ( pos,val, 2 * i + 1, lb, mid);
        }
        else {
            update (pos, val, 2 * i + 2, mid, rb);
        }
        tree[i] = min(tree[2 * i + 1], tree [2 * i + 2]);
    }
    long long get(int l, int r){
        return get(l,r,0,0,size);
    }
    long long get(int l, int r, int i, int lb, int rb) {
        if ( l <= lb && rb <= r) {
            return tree[i];
        }
        else if (lb >= r || rb <= l) {
            return INF;
        }
        return min(get(1, r, 2 * i + 1, lb, (lb + rb)/2), get(l,r,2 * i + 2, (lb + rb)/2, rb));
    }
};

void solve(){
    int n, m;
    cin >> n >> m;
    vector<int> c(n);
    for(int i=0; i<n; i++){
        cin >> c[i];
    }
    c[0] = 0; // start at the first city, current gas: M_i = M, i = 0.

    //create a segment tree
    segtree seg(n +m);
    for(int i = 0; i<n; i++) {

        // cost = minimun inside segment tree.
        long long cost  = seg.get(i, i + m);
        if (i == 0) cost = 0;

        // if we can reach the city and city has gas station, update till city [i+m]
        
        if (i == 0 || (c[i] && cost < INF)){
            seg.update(i + m, c[i] + cost);
        }
    }
    //calculate the minimun cost.
    long long ans = seg.get(n - 1, n + m);
    cout << (ans == INF ? -1 : ans) << '\n';
}

int main() {
    ios_base :: sync_with_stdio(0);
    cin.tie(0);
    freopen("running_on_fumes_chapter_1_input.txt", "r",stdin);
    freopen("running_on_fumes_chapter_1_output.txt", "w",stdout);
}