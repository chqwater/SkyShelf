<template>
	<div class="page-base">
		<div class="content-box-book">
			<div class="info">
				<div class="cover-pic">
				</div>
				<div class="info-detail">
					<p>Title:</p>
					<p>Author:</p>
					<p>Category:</p>
				</div>
			</div>
			<ElDivider content-position="left">Description</ElDivider>
			<div class="review">
				<p>This is a description. This is a description. This is a description. This is a description. This is a description. </p>
			</div>
			<ElDivider></ElDivider>
			<div class="bottom">
				<ElButton type="primary">Start reading</ElButton>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ElBreadcrumb, ElBreadcrumbItem, ElButton, ElDivider } from 'element-plus';

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