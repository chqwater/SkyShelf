<template>
    <div class="content-box-book">
      <div class="book" v-for="item in prop.bookList">
        <div class="cover" @click="openBook(item)" >
            <img :src="item.cover" alt="" style="width: 100%; height: 100%;">
        </div>
        <div class="title-b">
            {{ item.name }}
        </div>
      </div>
    </div>
</template>

<script setup lang="ts" name="booklist">
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const prop = reactive({
    bookList: [
        {
        name: "Harry Potter",
        bookid: 1,
        cover: "https://static.posters.cz/image/750webp/214933.webp",
        url: "https://kvongcmehsanalibrary.wordpress.com/wp-content/uploads/2021/07/harrypotter.pdf",
        currentPage: 100
        }
    ]
})

const openBook = (data:any)=>{
    router.push({
        path: '/bookcontent',
        query: {
            bookurl: "https://corsproxy.io/?"+data.url,
            bookid: data.bookid,
            currentPage: data.currentPage,
            name: data.name
        }
    })
}
</script>

<style scoped>
.content-box-book{
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    margin: 0;
    flex-wrap: wrap;
}
.book{
    width: 150px;
    height: 250px;
    margin: 15px;
}
.cover{
    width: 100%;
    height: 220px;
    border-radius: 15px;
    margin: 0 0 10px 0;
    cursor: pointer;
    overflow: hidden;
}
.cover:hover{
    box-sizing: border-box;
    border: 1px solid transparent;
    background-clip: padding-box;
    box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4); 
}
.title-b{
    display: flex;
    justify-content: center;
    font-family: cursive;
    font-size: 18px;
}
</style>
