<template>
    <div class="content-box-book">
      <div class="book" v-for="item in prop.bookList">
        <div class="cover" @click="" >
            <img :src="item.cover" alt="" style="width: 100%; height: 100%;">
        </div>
        <div class="title">
            {{ item.name }}
        </div>
      </div>
    </div>
</template>

<script setup lang="ts" name="booklist">
import { reactive, ref } from 'vue';

const prop = reactive({
    bookList: [
        {
        name: "Harry Potter",
        cover: "https://static.posters.cz/image/750webp/214933.webp"
        }
    ]
})
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
    border: 1px solid #409EFF;
}
.title{
    display: flex;
    justify-content: center;
    font-family: cursive;
    font-size: 18px;
}
</style>
