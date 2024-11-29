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
				<ElButton type="primary">Start reading</ElButton>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ElButton, ElDivider } from 'element-plus';
import { onMounted, reactive } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const param = reactive({
	category: null,
	book_id: null,
	title: '',
	author: '',
	description: '',
	file_url: '',
	img_url: ''
})

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