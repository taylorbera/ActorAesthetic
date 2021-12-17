document.write(`
<div class="container">
    <div class="row">
        <div class="col-md-12 col-sm-12">
            <div class="wow fadeInUp col-sm-6" data-wow-delay=".2s">
                <h2>Let's work together!</h2>
                <div class="contact-form">
                    <form id="contact-form" method="post" action="mailto:berataylor@gmail.com">
                        <label>
                            <input name="name" type="text" class="form-control" placeholder="Your Name" required>
                        </label>

                        <label>
                            <input name="email" type="email" class="form-control" placeholder="Your Email" required>
                        </label>

                        <label>
                            <textarea name="message" class="form-control" placeholder="Message" rows="4" required></textarea>
                        </label>

                        <div class="contact-submit">
                            <input type="submit" class="form-control submit" value="Send a message">
                        </div>
                    </form>
                </div>
            </div>
            <div class="wow fadeInUp col-sm-6"  data-wow-delay="0.3s">
                <h2>Actor Aesthetic - By Maggie Bera</h2>
                <ul class="social-icon wow fadeInUp">
					<li><a href="https://www.facebook.com/ActorAesthetic/" class="fa fa-facebook"></a></li>
					<li><a href="https://podcasts.apple.com/us/podcast/actor-aesthetic/id1441487750?mt=2" class="fa fa-apple"></a></li>
					<li><a href="https://www.instagram.com/actoraesthetic/" class="fa fa-headphones"></a></li>
                    <li><a href="" class="fa fa-envelope"></a></li>
				</ul>
            </div>
        </div>
    </div>
</div>
`);