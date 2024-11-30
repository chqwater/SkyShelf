<template>
  <div class="content-box-book">
		<div class="empty-state" v-if="prop.bookList.length === 0">
		<div class="empty-box" @click="handleFindBook">
			<p>Click Here</p>
			<ElIcon :size="100"><Collection /></ElIcon>
			<p>Find Your Book!😄</p>
		</div>
		</div>
    <div class="book" v-for="item in prop.bookList" v-else>
      <div class="cover" @click="openBook(item)">
        <img :src="item.img_url" alt="" style="width: 100%; height: 100%" />
      </div>
      <div class="title-b">
        {{ item.book_name }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts" name="booklist">
import { onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { ElIcon } from 'element-plus';
import { getShelf } from "../api";
import { ElLoading } from 'element-plus';

const router = useRouter();
const user_id: string | null = localStorage.getItem('vuems_id');
const prop = reactive({
  bookList: []
});
const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
const openBook = (data: any) => {
  router.push({
    path: "/bookcontent",
    query: {
      bookurl: "https://corsproxy.io/?" + data.file_url,
      bookid: data.book_id,
      currentPage: data.currentPage,
      name: data.book_name,
    },
  });
};
const handleFindBook = () => {
  router.push("/home/recommendation");
};
const loadShelf = async ()=>{
  await getShelf(user_id).then((res:any)=>{
    prop.bookList = res;
  })
  loading.close();
}
onMounted(()=>{
  loadShelf();
})
</script>

<style scoped>
.content-box-book {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
  margin: 0;
  flex-wrap: wrap;
}
.empty-state{
	display: flex;
	flex-direction: column;
	width: 100%;
	justify-content: center;
	align-items: center;
	font-size: 30px;
	font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
.empty-box{
	width: 300px;
	height: 300px;
	cursor: pointer;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	border-radius: 50px;
}
.empty-box:hover{
	color: #409EFF;
	box-sizing: border-box;
  background-clip: padding-box;
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4); 
}
.book {
  width: 150px;
  height: 250px;
  margin: 15px;
}
.cover {
  width: 100%;
  height: 220px;
  border-radius: 15px;
  margin: 0 0 10px 0;
  cursor: pointer;
  overflow: hidden;
}
.cover:hover {
  box-sizing: border-box;
  border: 1px solid transparent;
  background-clip: padding-box;
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4);
}
.title-b {
  display: flex;
  justify-content: center;
  font-family: cursive;
  font-size: 18px;
}
</style>
