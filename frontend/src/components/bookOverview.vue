<template>
	<div class="page-base">
		<div class="content-box-book">
			<div class="info">
				<div class="cover-pic">
					<img :src="param.img_url" alt="" style="width: 100%; height: 100%">
				</div>
				<div class="info-detail">
					<p>Title: {{ param.title }}</p>
					<p>Author: {{ param.author }}</p>
					<p>Category: {{ param.category }}</p>
				</div>
			</div>
			<ElDivider content-position="left">Description</ElDivider>
			<div class="review">
				<p>{{ param.description }}</p>
			</div>
			<ElDivider></ElDivider>
			<div class="bottom">
				<ElButton type="primary" @click="addToShelf">Add book to my shelf</ElButton>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ElButton, ElDivider } from 'element-plus';
import { onMounted, reactive } from 'vue';
import { useRoute } from 'vue-router';
import { useRouter } from "vue-router";
import { ElNotification as notify } from 'element-plus';
import { addBook } from '../api';
import { ElLoading } from 'element-plus';

const route = useRoute();
const router = useRouter();
const user_id: string | null = localStorage.getItem('vuems_id');
const param = reactive({
	category: null as any,
	book_id: null as any,
	title: '' as any,
	author: '' as any,
	description: '' as any,
	file_url: '' as any,
	img_url: '' as any
})

const addToShelf = async ()=>{
	const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  	})
	await addBook({
		user_id: user_id,
		book_id: param.book_id
	})
	console.log('add');
	loading.close();
	router.push('/home/booklist')
}
onMounted(()=>{
	param.category = route.query.category;
	param.book_id = route.query.book_id;
	param.title = route.query.title;
	param.author = route.query.author;
	param.description = route.query.description;
	param.img_url = route.query.img_url;
	param.file_url = route.query.file_url;
})
</script>

<style scoped>
.page-base{
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
	position: relative;
}
.content-box-book{
	background-color: white;
	border-radius: 40px;
	height: 600px;
	width: 600px;
	padding: 10px;
  	box-shadow: 0 0 10px 5px white;
}
.info{
	height: 30%;
	display: flex;
	flex-direction: row;
}
.cover-pic{
	background-color: gray;
	height: 100%;
	width: 120px;
	border-radius: 20px;
	margin-left: 10px;
	margin-right: 20px;
}
.info-detail{
	display: flex;
	flex-direction: column;
	justify-content: center;
}
.review{
	height: 45%;
}
.bottom{
	display: flex;
	align-items: end;
	height: 5%;
	justify-content: end;
	padding-right: 10px;
}
</style>